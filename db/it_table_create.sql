-- Just a file to hold all the commands to create the table I need for IT
-- Create a new database called 'IT_2019'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
    SELECT name
        FROM sys.IT_2019 databases
        WHERE IT_2019 = N'IT_2019'
)
CREATE DATABASE it_2019
GO

CREATE TABLE 
