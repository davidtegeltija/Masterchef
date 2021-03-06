%rebase("bootstrap.tpl")

%if len(vseckane_slike) != 0:
    %for recept in vseckani_recepti:
    <div class="container section">
        <div class="row" style="margin-top: 7%; margin-bottom: 7%;">
            <div class="col-md-6" style="background: #e0dcdc; padding: 5%;">
                <h3 class="text-center">
                    {{recept[1]}}
                </h3>
                <p>
                    <b>Avtor: {{recept[0]}}</b>
                </p>
                <b>Sestavine</b>
                <ul>
                    %for i in recept[2]:
                    <li>{{i}}</li>
                    %end
                </ul>
                <p style="margin-top: 10%; margin-bottom: auto;">
                    <b>Postopek</b>
                    <br>
                    {{recept[3]}}
                </p>
            </div>
            <div class="col-md-6" style="background: #e0dcdc; padding: 5%;">
                <div style="width: 100%">
                    <img src="/static/{{recept[4]}}" style="width: 100%; height: auto;"/>
                </div>
                <div style="padding-top: 5%; padding-bottom: 5%;">
                    <div class="text-center">
                        <form method="POST" action="/odstrani" enctype=multipart/form-data>
                            <button class="btn btn-primary" type="submit" name="odstrani" value="{{recept[1]}}" enctype="multipart/form-data">Odstrani ta recept</button>  
                        </form> 
                    </div>                   
                </div>                
            </div> 
        </div>
    </div>
    %end    
%else:
<div class="container">
    <div class="row">
        <div class="col mx-auto">
            <div class="text-center">
                <br>
                <h1>Všečkali niste še nobenih receptov.</h1>
                <br>
            </div>
        </div>
    </div>  
</div>  
%end





