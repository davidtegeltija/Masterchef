%rebase("bootstrap.tpl")

<h3> Tukaj lahko dodate svoj recept in ga delite z drugimi obiskovalci te spletne strani </h3>
<p>
    Lahko uporabite svoje podatke ali pa kakšen pvsedonim. Če želite, lahko svoj izdelek tudi slikate
    in to delite z ostalimi.
</p>

<form method="POST" action="/dodaj_recept" enctype=multipart/form-data>
  <div class="container">
    <b>Vaša ime in priimek</b>
      <div class="col col-lg-2">
        <input type="text" class="form-control" placeholder="Ime" name="Ime">
      </div>
      <div class="col col-lg-2">
        <input type="text" class="form-control" placeholder="Priimek" name="Priimek">
      </div>
    <br>  
    <b>Kako se imenuje vaša hrana?</b>
      <div class="col col-lg-2">
        <input type="text" class="form-control" placeholder="Naslov recepta" name="Naslov">
      </div> 
    <br>   
      <div class="row">
        <b>Sem napišite svoj recept</b>
        <ul>
        <div class="col">      
          <br>
          <li> <b>Sestavine</b></li>
          <textarea id="text" class="form-control" name="Sestavine" rows="5" cols="48" placeholder="Vsako sestavino in njeno količino napišite v svojo vrstico in pred njo postavite -, kot kaže primer. &#10 Primer: &#10 -1kg krompirja &#10 -500g piščanca"></textarea>
          <br>
          <li><b>Postopek</b></li>
          <textarea id="text" class="form-control" name="Postopek" rows="7" cols="48"></textarea>
        </div>
        </ul>
      </div>
  
    <div class="input-group">
        <input type=file name="Slika" accept=".jpg, .png, .jpeg" class="form-control" id="inputGroupFile02">
    </div>
    <br>
    <button class="btn btn-primary" type="submit" value="Upload">Naloži</button>
  </div>
</form>

