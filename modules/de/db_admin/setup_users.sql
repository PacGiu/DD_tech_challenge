CREATE ROLE ds_user_role;
CREATE USER ds_user PASSWORD 'ds_user';
GRANT ds_user_role TO ds_user;
GRANT USAGE ON SCHEMA public TO ds_user_role;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO ds_user_role;


CREATE ROLE mle_user_role;
CREATE USER mle_user PASSWORD 'mle_user';
GRANT mle_user_role TO mle_user;
GRANT ALL PRIVILEGES ON SCHEMA public TO mle_user_role;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO mle_user_role;
