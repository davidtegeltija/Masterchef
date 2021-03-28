%rebase("bootstrap.tpl")


<form method="POST" action="/shrani" enctype=multipart/form-data>
    <div class="container section">
        <div class="row" style="margin-top: 7%; margin-bottom: 7%;">
            <div class="col-md-6" style="background: #e0dcdc; padding: 5%;">
                <h3 class="text-center">
                    {{recept[1]}}
                </h3>
                <p>
                    <b>Avtor: {{recept[0]}}</b>
                </p>
                <div class="col">
                <b>Sestavine</b>
                    <textarea class="form-control" name="Nove_sestavine"  rows="5" cols="48">
                    %for i in recept[2]:
                    &#10 -{{i}} 
                     %end
                    </textarea>
               
                </div> 
               
                <p style="margin-top: 10%; margin-bottom: auto;">
                    <b>Postopek</b>
                    <textarea class="form-control" name="Nov_postopek"  rows="5" cols="55">{{recept[3]}}</textarea>
                </p>
            </div>
            <div class="col-md-6" style="background: #e0dcdc; padding: 5%;">
                <div style="width: 100%">
                    <img src="/static/{{recept[4]}}" style="width: 100%; height: auto;"/>
                    <br>
                    <br>
                    <b>Spremenite sliko tukaj:</b>
                    <input type=file name="Nova_slika" accept=".jpg, .png, .jpeg" class="form-control" id="inputGroupFile02">
                </div>
                               
            </div> 
        </div>
    </div>
    <div class="text-center">
        <button class="btn btn-primary" type="submit" enctype="multipart/form-data">Shrani spremembe</button> 
    </div>
</form>
                        
