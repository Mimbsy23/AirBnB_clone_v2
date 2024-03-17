-- This create a database hbnb_test_db with the user hbnb_test in localhost
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS "hbnb_test"@"localhost" identified by "hbnb_test_pwd";
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO "hbnb_test"@"localhost";
GRANT SELECT ON performance_schema.* TO "hbnb_test"@"localhost";

