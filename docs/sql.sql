CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL
);

CREATE TABLE teams (
    team_id UUID PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL
);

CREATE TABLE user_team (
    user_team_id UUID PRIMARY KEY,
    team_id UUID NOT NULL, 
    user_id UUID NOT NULL,
    CONSTRAINT fk_team FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE donation_opt (
    donation_opt_id UUID PRIMARY KEY,
    donation_name VARCHAR(100) NOT NULL, 
    donation_points INT NOT NULL
);

CREATE TABLE donations (
    donation_id UUID PRIMARY KEY,
    donation_opt_id UUID NOT NULL,
    user_id UUID NOT NULL,       
    donation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    quant INT NOT NULL DEFAULT 1, 
    CONSTRAINT fk_donation_opt FOREIGN KEY (donation_opt_id) REFERENCES donation_opt(donation_opt_id),
    CONSTRAINT fk_donation_user FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE donation_logs (
    
    log_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID,
    donation_opt_id UUID,
    quantity INTEGER,
    ip_address VARCHAR(45),          
    user_agent TEXT,                 
    browser_language VARCHAR(10),    
    screen_resolution VARCHAR(20),   
    timezone VARCHAR(50),           
    session_referrer TEXT,          
    http_status INTEGER,           
    is_success BOOLEAN,
    error_message TEXT,           
    created_at TIMESTAMP
);

INSERT INTO donation_opt (donation_opt_id, donation_name, donation_points) VALUES
(gen_random_uuid(), 'Gorro', 1),
(gen_random_uuid(), 'Luva', 1),
(gen_random_uuid(), 'Cachecol', 1),
(gen_random_uuid(), 'Meia', 1),
(gen_random_uuid(), 'Kit Acessorios', 5),
(gen_random_uuid(), 'Racao para pets 2,5kg', 5),
(gen_random_uuid(), 'Kit higiene (50 unidades)', 10),
(gen_random_uuid(), 'Camiseta de manga curta', 10),
(gen_random_uuid(), 'Jogo de lençol completo', 10),
(gen_random_uuid(), 'Toalhas', 10),
(gen_random_uuid(), 'Kit descartavel para sopa (50 unidades)', 10),
(gen_random_uuid(), 'Calca', 15),
(gen_random_uuid(), 'Moletom', 15),
(gen_random_uuid(), 'Jaqueta', 15),
(gen_random_uuid(), 'Camiseta de manga longa', 15),
(gen_random_uuid(), 'Blusa de manga comprida', 15),
(gen_random_uuid(), 'Casaco', 15),
(gen_random_uuid(), 'Sapato', 15),
(gen_random_uuid(), 'Cobertor', 15),
(gen_random_uuid(), 'Racao para pets 10kg', 15),
(gen_random_uuid(), 'Outros - 1 ponto', 1),
(gen_random_uuid(), 'Outros - 5 pontos', 5),
(gen_random_uuid(), 'Outros - 10 pontos', 10),
(gen_random_uuid(), 'Outros - 15 pontos', 15);