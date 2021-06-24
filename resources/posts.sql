CREATE TABLE IF NOT EXISTS public.posts (
    id SERIAL PRIMARY KEY,
    external_id UUID NOT NULL DEFAULT gen_random_uuid(),
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone,
    title character varying(255) NOT NULL,
    summary text NOT NULL,
    body text NOT NULL,
    is_deleted boolean NOT NULL
);
