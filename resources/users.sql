CREATE TABLE IF NOT EXISTS public.users (
    id SERIAL PRIMARY KEY,
    external_id UUID NOT NULL DEFAULT gen_random_uuid(),
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone,
    first_name character varying(255) NOT NULL,
    last_name character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    password character varying(255) NOT NULL
);

INSERT INTO users(first_name, last_name, email, password) VALUES
('Bob', 'Smith', 'bob.smith@mail.com', 'password123'),
('Mark', 'Johnson', 'mark.johnson@mail.com', 'password1234');
