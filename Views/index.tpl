%rebase("bootstrap.tpl")


%if uporabnik != "Gost":
    %for oseba in podatki[::-1]:
    <div class="container section">
        <div class="row" style="margin-top: 7%; margin-bottom: 7%;">
            <div class="col-md-6" style="background: #e0dcdc; padding: 5%;">
                <h3 class="text-center">
                    {{oseba[1]}}
                </h3>
                <p>
                    <b>Avtor: {{oseba[0]}}</b>
                </p>
                <b>Sestavine</b>
                <ul>
                    %for i in oseba[2]:
                    <li>{{i}}</li>
                    %end
                </ul>
                <p style="margin-top: 10%; margin-bottom: auto;">                
                    <b>Postopek</b>
                    <br>
                    {{oseba[3]}}
                </p>
            </div>
            <div class="col-md-6" style="background: #e0dcdc; padding: 5%;">
                <div style="width: 100%">
                    <img src="/static/{{oseba[4]}}" style="width: 100%; height: auto;"/>
                </div>
                %if oseba[1] not in vseckani_recepti and oseba[1] not in nevseckani_recepti:
                    <div style="padding-top: 5%; padding-bottom: 5%;">
                        <ul class="list-group">
                            <li class="list-group-item">
                                <form method="POST" action="/glasuj_za" enctype=multipart/form-data>
                                    <button class="btn btn-primary" type="submit" name="ja" value="{{oseba[1]}}" enctype="multipart/form-data">Všeč mi je</button>
                                    {{oseba[5]}} 
                                </form> 
                            </li>
                            <li class="list-group-item">
                                <form method="POST" action="/glasuj_proti" enctype=multipart/form-data>
                                    <button class="btn btn-primary" type="submit" name="ne" value="{{oseba[1]}}">Ni mi všeč</button>
                                    {{oseba[6]}} 
                                </form>
                            </li>  
                        </ul>
                    </div>
                %elif oseba[1] in vseckani_recepti:
                    <div style="padding-top: 5%; padding-bottom: 5%;">
                        <h4 class="text-center">
                            Ta recept vam je všeč
                        </h4>
                    </div>
                %else:
                    <div style="padding-top: 5%; padding-bottom: 5%;">
                        <h4 class="text-center">
                            Ta recept vam ni všeč
                        </h4>                
                    </div>
                %end
            </div>
            <div class="col" style="background: #e0dcdc; padding: 5%;"> 
                <p>
                    <b>Komentarji:</b>
                </p>
                <ul>
                    %for komentar in oseba[7]:
                    <li>{{komentar}}</li>
                    %end
                </ul>
                <p>
                    <b>Dodajte svoj komentar</b>
                </p>
                <form method="POST" action="/komentiraj/{{oseba[1]}}" enctype=multipart/form-data>
                    <textarea class="form-control" name="Komentar"></textarea>
                    <br>
                    <button class="btn btn-primary" type="submit" enctype="multipart/form-data">Dodaj komentar</button> 
                </form>
            </div>
        </div>
    </div>
    %end
%else:
    %for oseba in podatki[::-1]:
    <div class="container section">
        <div class="row" style="margin-top: 7%; margin-bottom: 7%;">
            <div class="col-md-6" style="background: #e0dcdc; padding: 5%;">
                <h3 class="text-center">
                    {{oseba[1]}}
                </h3>
                <p><b>Avtor: {{oseba[0]}}</b></p>
                <b>Sestavine</b>
                <ul>
                    %for i in oseba[2]:
                    <li>{{i}}</li>
                    %end
                </ul>
                <p style="margin-top: 10%; margin-bottom: auto;">                
                    <b>Postopek</b>
                    <br>
                    {{oseba[3]}}
                </p>
            </div>
            <div class="col-md-6" style="background: #e0dcdc; padding: 5%;">
                <div style="width: 100%">
                    <img src="/static/{{oseba[4]}}" style="width: 100%; height: auto;"/>
                </div>
                <div style="padding-top: 5%; padding-bottom: 5%;">
                    <ul class="list-group">
                        <li class="list-group-item">
                            <form method="POST" action="/glasuj_za" enctype=multipart/form-data>
                                <button class="btn btn-primary" type="submit" name="ja" value="{{oseba[1]}}" enctype="multipart/form-data">Všeč mi je</button>
                                {{oseba[5]}} 
                            </form> 
                        </li>
                        <li class="list-group-item">
                            <form method="POST" action="/glasuj_proti" enctype=multipart/form-data>
                                <button class="btn btn-primary" type="submit" name="ne" value="{{oseba[1]}}">Ni mi všeč</button>
                                {{oseba[6]}} 
                            </form>
                        </li>  
                    </ul>
                </div>                
            </div>
            <div class="col" style="background: #e0dcdc; padding: 5%;"> 
                <p>
                    <b>Komentarji:</b>
                </p>
                <ul>
                    %for komentar in oseba[7]:
                    <li>{{komentar}}</li>
                    %end
                </ul>
                <p>
                    <b> Če želite komentirati recept se prijavite na spletno stran.</b>
                </p>
            </div> 
        </div>
    </div>
%end

