%rebase("bootstrap.tpl")

%if len(vasi_recepti) == 0:
<div class="container">
    <div class="row">
        <div class="col mx-auto">
            <div class="text-center">
                <br>
                <h1>Na spletno stran niste dodali še nobenega recepta.</h1>
                <br>
            </div>
        </div>
    </div>  
</div>  
%else:
%for recept in vasi_recepti:
    <div class="container section">
        <div class="row" style="margin-top: 7%; margin-bottom: 7%;">
            <div class="col-md-6" style="background: #e0dcdc; padding: 5%;">
                <h3 class="text-center">
                    {{recept[1]}}
                </h3>
                <p>Avtor: {{recept[0]}}</p>
                <ul>
                    %for i in recept[2]:
                    <li>{{i}}</li>
                    %end
                </ul>
                <p style="margin-top: 10%; margin-bottom: auto;">
                    {{recept[3]}}
                </p>
            </div>
            <div class="col-md-6" style="background: #e0dcdc; padding: 5%;">
                <div style="width: 100%">
                    <img src="/static/{{recept[4]}}" style="width: 100%; height: auto;"/>
                </div>
                <div style="padding-top: 5%; padding-bottom: 5%;">
                    <div class="text-center">
                        <form method="GET" action="/uredi/{{recept[1]}}" enctype=multipart/form-data>
                            <button class="btn btn-primary" type="submit"  enctype="multipart/form-data">Uredi svoj recept</button>  
                        </form> 
                    </div>                   
                </div>                
            </div> 
        </div>
    </div>
%end

