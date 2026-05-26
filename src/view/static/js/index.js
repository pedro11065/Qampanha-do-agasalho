lucide.createIcons();
const API_URL = "http://127.0.0.1:5000";

// 1. NEVE ANIMADA
function createSnow() {
    const container = document.getElementById('snow-container');
    const count = 50;
    for (let i = 0; i < count; i++) {
        const snow = document.createElement('div');
        snow.className = 'snowflake';
        const size = Math.random() * 4 + 2 + 'px';
        snow.style.width = size;
        snow.style.height = size;
        snow.style.left = Math.random() * 100 + '%';
        snow.style.animationDuration = (Math.random() * 7 + 5) + 's';
        snow.style.animationDelay = (Math.random() * 5) + 's';
        snow.style.opacity = Math.random() * 0.7 + 0.3;
        container.appendChild(snow);
    }
}

// 2. ALTERNAR ABAS COM ANIMAÇÃO E REDIMENSIONAMENTO
function switchTab(tab) {
    const container = document.getElementById('main-container');
    const sections = ['donation', 'teams', 'user'];
    
    // Transição de largura do container
    if (tab === 'teams') {
        container.classList.replace('max-w-xl', 'max-w-6xl');
    } else {
        container.classList.replace('max-w-6xl', 'max-w-xl');
    }

    sections.forEach(s => {
        const section = document.getElementById(`section-${s}`);
        const btn = document.getElementById(`btn-tab-${s}`);
        
        if (s === tab) {
            section.classList.remove('hidden');
            section.classList.add('section-animate');
            btn.classList.add('active');
            btn.classList.remove('text-gray-400');
        } else {
            section.classList.add('hidden');
            section.classList.remove('section-animate');
            btn.classList.remove('active');
            btn.classList.add('text-gray-400');
        }
    });
}

// 3. TOAST NOTIFICATION
function showToast(msg, isError = false) {
    const toast = document.getElementById('toast');
    toast.textContent = msg;
    toast.className = `mb-6 p-4 rounded-2xl text-center font-medium animate-slide-up ${isError ? 'bg-red-500/10 text-red-500 border border-red-500/20' : 'bg-green-500/10 text-green-600 border border-green-500/20'}`;
    toast.classList.remove('hidden');
    setTimeout(() => toast.classList.add('hidden'), 6000);
}

// 4. QLIK CLOUD RELOAD
async function triggerQlikReload() {
    const qlikUrl = 'https://phsq.br.qlikcloud.com/api/v1/automations/1835d6d4-343f-43fa-83fc-e2975c5f6775/actions/execute';
    const qlikToken = '35H75OAzz3vhLwah3XBm1wbwvVQ2SdHDNSEikeEZbqzNxf8Qk8hRiITJ5kawlrLb';
    try {
        await fetch(qlikUrl, {
            method: 'POST',
            headers: { 'X-Execution-Token': qlikToken, 'Content-Type': 'application/json' }
        });
    } catch (error) { console.error("Falha na conexão com Qlik:", error); }
}

// 5. CARREGAR DADOS
async function fetchData() {
    try {
        const resTeam = await fetch(`/team/search`);
        const jsonTeam = await resTeam.json();
        if (jsonTeam.ok) {
            const selects = [document.getElementById('selectTeam'), document.getElementById('selectTeamForUser')];
            jsonTeam.data.forEach(t => selects.forEach(s => s.add(new Option(t[1], t[0]))));
        }

        const resOpt = await fetch(`/donation/searchOpt`);
        const jsonOpt = await resOpt.json();
        if (jsonOpt.ok) {
            const select = document.getElementById('selectOpt');
            jsonOpt.data.forEach(i => select.add(new Option(`${i[1]} (${i[2]} pts)`, i[0])));
        }
    } catch (e) { showToast(`Erro de carregamento inicial`, true); }
}

// 6. BUSCAR USUÁRIOS POR TIME
document.getElementById('selectTeam').addEventListener('change', async (e) => {
    const teamId = e.target.value;
    const userSelect = document.getElementById('selectUser');
    userSelect.innerHTML = '<option value="">Buscando usuários...</option>';
    userSelect.disabled = true;
    if (!teamId) return;
    try {
        const res = await fetch(`/user/searchByTeam`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ team_id: teamId })
        });
        const json = await res.json();
        userSelect.innerHTML = '<option value="">Selecione o doador...</option>';
        if (json.ok) {
            json.data.forEach(u => userSelect.add(new Option(u[1], u[0])));
            userSelect.disabled = false;
        }
    } catch (e) { showToast(`Erro ao buscar usuários`, true); }
});

// 7. REGISTRAR DOAÇÃO (COM AUDITORIA)
function getBrowserMetadata() {
    return {
        browser_language: navigator.language || navigator.userLanguage,
        screen_resolution: `${window.screen.width}x${window.screen.height}`,
        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
        referrer: document.referrer || "Direct Access"
    };
}

document.getElementById('formDonation').addEventListener('submit', async (e) => {
    e.preventDefault();
    const donationOptId = document.getElementById('selectOpt').value;
    const userId = document.getElementById('selectUser').value;
    const quantTyped = parseInt(document.getElementById('inputQuant').value);
    const btn = document.getElementById('btnDonation');
    const originalText = btn.innerHTML;

    btn.disabled = true;
    let successCount = 0;

    for (let i = 1; i <= quantTyped; i++) {
        btn.innerHTML = `Enviando ${i} de ${quantTyped}...`;
        const metadata = getBrowserMetadata();
        
        try {
            const res = await fetch(`/donation/create`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ 
                    donation_opt_id: donationOptId, 
                    user_id: userId, 
                    quant: quantTyped, 
                    browser_info: metadata 
                })
            });
            if (res.ok) successCount++;
        } catch (err) { break; }
    }

    if (successCount === quantTyped) {
        btn.innerHTML = "Sincronizando Qlik...";
        await triggerQlikReload();
        showToast(`Sucesso! ${successCount} registros feitos.`);
        e.target.reset();
        document.getElementById('selectUser').disabled = true;
    } else {
        showToast(`Falha parcial ou total no registro`, true);
    }
    btn.disabled = false;
    btn.innerHTML = originalText;
});

// 8. CADASTRAR USUÁRIO
document.getElementById('formUser').addEventListener('submit', async (e) => {
    e.preventDefault();
    try {
        const res = await fetch(`/user/create`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ 
                user_name: document.getElementById('newUserName').value, 
                team_id: document.getElementById('selectTeamForUser').value 
            })
        });
        const json = await res.json();
        if (json.ok) {
            showToast("Usuário cadastrado com sucesso!");
            e.target.reset();
            switchTab('donation');
        }
    } catch (e) { showToast(`Erro ao criar usuário`, true); }
});

window.onload = () => {
    fetchData();
    createSnow();
};