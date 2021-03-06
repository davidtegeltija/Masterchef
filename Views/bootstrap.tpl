<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    
    <title>Masteršef</title>
  </head>
  
  <body>
    <div class="container">
      <h1 style="text-align: center;">Masteršef</h1>
      <br>
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark" >
          <div class="container-fluid">
              <div class="collapse navbar-collapse" >
                  <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                      <li class="nav-item" style="margin: 2px 10px 2px 10px;">
                          <a class="nav-link" href="/">Recepti</a>
                      </li>
                      <li class="nav-item" style="margin: 2px 10px 2px 10px;">
                          <a class="nav-link" href="/vseckano">Všečkani recepti</a>
                      </li>
                      <li class="nav-item" style="margin: 2px 10px 2px 10px;">
                          <a class="nav-link" href="/dodaj">Dodajte svoj recept</a>
                      </li>                
                      %if uporabnik != "Gost":
                      <li class="nav-item" style="margin: 2px 10px 2px 10px;">
                          <a class="nav-link" href="/vasi_recepti">Vaši recepti</a>
                      </li>
                      <li class="nav-item dropdown" style="margin: 2px 10px 2px 10px;">
                        <a class="nav-link dropdown-toggle" id="navbarDropdown" role="button" data-bs-toggle="dropdown">
                          Prijavljeni ste kot <b>{{uporabnik}} </b>
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">                          
                          <li><a class="dropdown-item" href="/spremenite_geslo">Spremenite geslo</a></li>  
                          <li><a class="dropdown-item" href="/odjava">Odjava</a></li>                        
                        </ul>
                      </li>                     
                      %else:
                      <li class="nav-item" style="margin: 2px 10px 2px 10px;">
                        <a class="nav-link" href="/prijava">Prijavite se</a>
                      </li>
                      %end
                  </ul>
              </div>
          </div>
      </nav>
      <br>
    {{!base}}
    </div>

    <br>
    <br>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
  </body>
</html>