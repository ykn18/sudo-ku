# Sudo-ku
## Advanced Programming Languages 2019-2020
### Arena Gianluca - Lo Castro Alex	
#### Deployment
Per effettuare il deploy del backend, assumendo che Docker e Docker Compose siano installati:

    docker-compose up --build
 O nel caso in cui si voglia testare l'applicazione con una board quasi completa:

    docker-compose -f docker-compose-full.yml up --build
E' necessario che le porte 8080, 5050, 5000 e 27017 siano libere per fare il deploy dei server.
Per eseguire il frontend, qualora non fosse presente, è necessario installare [PyQt5](https://www.learnpyqt.com/installation/). 
Si consiglia di seguire il link fornito dato che l'installazione differisce leggermente tra sistemi operativi diversi.
A questo punto si può eseguire:

    cd frontend
    pip install -r requirements.txt
    python sudoku.py

 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYyMDA3OTg3MCwtMjI4NDU1NjU2XX0=
-->