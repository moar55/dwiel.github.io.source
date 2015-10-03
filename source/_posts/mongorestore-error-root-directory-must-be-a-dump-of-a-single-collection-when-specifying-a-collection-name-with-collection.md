title: " mongorestore: ERROR: root directory must be a dump of a single collection when specifying a collection name with --collection "
tags:
---


mongorestore wants the specific collection's filename rather than the entire database's dump folder:

<style>span, strong { font-family: courier, monospace; }</style>

*dwiel@dwiel$* mongodump -d db -c variables -o ../backups/1
connected to: 127.0.0.1
DATABASE: db	 to 	../backups/1/db
        db.variables to ../backups/1/db/variables.bson
                3 objects
*dwiel@dwiel$* mongorestore -d db -c variables --drop ../backups/1
ERROR: root directory must be a dump of a single collection
       when specifying a collection name with --collection
usage: ........
*dwiel@dwiel$* mongorestore -d db -c variables --drop ../backups/1/db/variables.bson
connected to: 127.0.0.1
../backups/1/db/variables.bson
        going into namespace [db.variables]
        dropping
        3 objects


