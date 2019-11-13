# Purpose
Explore the internals of ODBC

# What is [ODBC](https://docs.microsoft.com/en-us/sql/odbc/microsoft-open-database-connectivity-odbc?view=sql-server-2017)?
ODBC is a specification for a database API creating a standard way for applications to interact with various databases via a series of translation and application layers. It is independent of any specific database, language or operating system.

Architecture

```
         Application Layer 
       (Python in this repo)
                |
                |
                |
      ODBC API Language Wrapper 
        (PyODBC for this repo)
                |
                |
                |
         Driver Manager 
      (unixODBC + odbcinst.ini)
                |
                |
                |
            ODBC Driver 
      (referenced in odbc.ini)
                |
                |
                |
             Database
(Postgres and SQL Server for this repo)
```

### Instructions
Install ODBC driver manager
```bash
brew install unixODBC
```

Install ODBC drivers
```bash
brew install psqlodbc
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
brew install msodbcsql17 mssql-tools
```

Configure ODBC connections
```bash
odbcinst -j
vim odbcinst.ini
vim odbc.ini
```

Pull the repo
```bash
git pull https://gitlab.com/AlexHagerman/what-is-odbc
```

Confirm connection settings
```bash
docker-compose -f stack.yml up -d
isql -v MSSQLDockerODBCDemo SA d3m0p@ssw0rd
select top 1 * from information_schema.columns;
quit
```

Explore ODBC with Python
```bash
poetry install
CFLAGS='-Wall -O0 -g' python setup.py build
lldb -f python -- -m pdb main.py

breakpoint set --file connection.cpp --line 232
breakpoint set --file connection.cpp --line 52
breakpoint set --file cursor.cpp --line 1100
breakpoint set --file getdata.cpp --line 776

run
```

