%rebase("bootstrap.tpl")

<form method="POST" action="/logiraj_me" enctype=multipart/form-data>
    <div class="container">
        <div class="row">
            <div class="col-3 mx-auto">
                <div class="text-center">
                    <h3>Prijavite se</h3>
                    <div class="col">
                        <input type="text" class="form-control" placeholder="Uporabniško ime" name="Uporabnisko_ime">
                    </div>
                    <div class="col">
                        <input type="password" class="form-control" placeholder="Geslo" name="Geslo">
                    </div>
                    <br>
                    <button class="btn btn-primary" type="submit" value="login">Logiraj me</button>
                </div>
            </div>
        </div>  
    </div> 
  </form>
<br>

<form method="GET" action="/nov_profil">
    <div class="container">
        <div class="row">
            <div class="col mx-auto">
                <div class="text-center">
                    <br>
                    <br>
                    <h3>Če nimate svojega profila ga ustvarite tukaj</h3>
                    <br>
                    <button class="btn btn-primary" enctype="multipart/form-data">Ustvarite nov profil</button>
                </div>
            </div>
        </div>  
    </div>    
 </form>