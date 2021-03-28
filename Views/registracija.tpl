%rebase("bootstrap.tpl")

<h3>Pozdravljeni na spletni strani Masteršef.</h3>
<p>
    Če želite po spletni strani iskati recepte, jih všečkati in ustvariti lastno zbirko všečkanih receptov si 
    ustvarite svoj osebni profil. 
</p>

<form method="POST" action="/logiraj_me" enctype=multipart/form-data>
    <div class="container">
        <div class="row">
            <div class="col-3 mx-auto">
                <div class="text-center">
                    <div class="col">
                        <input type="text" class="form-control" placeholder="Uporabniško ime" name="Novo_uporabnisko_ime">
                    </div>
                    <div class="col">
                        <input type="password" class="form-control" placeholder="Geslo" name="Novo_geslo">
                    </div>
                    <br>
                    <button class="btn btn-primary" type="submit" value="login">Ustvari profil</button>
                </div>
            </div>
        </div>  
    </div> 
</form>