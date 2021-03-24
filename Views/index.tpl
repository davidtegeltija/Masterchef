%rebase("bootstrap.tpl")



%for oseba in podatki[::-1]:
<div class="container section">
    <div class="row" style="margin-top: 7%; margin-bottom: 7%;">
        <div class="col-md-6" style="background: #e0dcdc; padding: 5%;">
            <h3 class="text-center">
                {{oseba[2]}}
            </h3>
            <p>Avtor: {{oseba[0]}} {{oseba[1]}}</p>
            <ul>
                %for i in oseba[3]:
                <li>{{i}}</li>
                %end
            </ul>
            <p style="margin-top: 10%; margin-bottom: auto;">
                {{oseba[4]}}
            </p>
        </div>
        <div class="col-md-6" style="background: #e0dcdc; padding: 5%;">
            <div style="width: 100%">
                <img src="/static/{{oseba[5]}}" style="width: 100%; height: auto;"/>
            </div>
            <div style="padding-top: 5%; padding-bottom: 5%;">
                <ul class="list-group">
                    <li class="list-group-item">
                        <form method="POST" action="/glasuj_za" enctype=multipart/form-data>
                            <button class="btn btn-primary" type="submit" name="ja" value="{{oseba[2]}}" enctype="multipart/form-data">Všeč mi je</button>
                            {{oseba[6]}} 
                        </form> 
                    </li>
                    <li class="list-group-item">
                        <form method="POST" action="/glasuj_proti" enctype=multipart/form-data>
                            <button class="btn btn-primary" type="submit" name="ne" value="{{oseba[2]}}">Ni mi všeč</button>
                            {{oseba[7]}} 
                        </form>
                    </li>  
                </ul>
            </div>
        </div> 
    </div>
</div>
%end
