%rebase("bootstrap.tpl")

<h3 class="text-center">Spremenite geslo svojega Mastešef profila</h3>
<br>
<br>

<form method="POST" action="/spremenite_geslo" enctype=multipart/form-data>
    <div class="container">
        <div class="row">
            <div class="col-3 mx-auto">
                <div class="text-center">
                    <div class="col">
                        <input type="text" class="form-control" placeholder="Staro geslo" name="Staro_geslo">
                    </div>                    
                    <div class="col">
                        <input type="text" class="form-control" placeholder="Novo_geslo" name="Novo_geslo">
                    </div>
                    <br>
                    <button class="btn btn-primary" type="submit">Spremenite geslo</button>
                </div>
            </div>
        </div>  
    </div> 
</form>