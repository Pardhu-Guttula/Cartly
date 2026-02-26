# Epic Title: Establish Scalable Infrastructure using Next.js, Node.js, and PostgreSQL

CREATE TABLE IF NOT EXISTS data (
    id SERIAL PRIMARY KEY,
    key VARCHAR(255) NOT NULL,
    value TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);