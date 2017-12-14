%include('header1.tpl')
<div class="container">
    <h2>Dar de Alta a un Usuario</h2>
  <div class="row">
      <div class="col-lg-4 col-sm-6 wow fadeInLeft delay-05s">
        <div class="service-list">
          <div class="service-list-col1"><i class="fa-institution"></i></div>
          <div class="service-list-col2">

            <form action="/registro" method="post" style="float: left">
                <label>Nombre Completo: </label><input type="text" name="usuario" required/><br>
                <label>N. sitio Web: </label><input type="text" name="usuario" required/><br>
                <label>Nombre Usuario : </label><input type="text" name="usuario" required/><br>
                <label>Contraseña: </label> <input type="password" name="clave" required/><br>
                <label>Definir lugar donde se va a almacenar los datos del hosting: </label>
                <select class="" name="sitio">
                  <option selected value="0"> Elige una opción </option>
                  <option value="1">FTP</option>
                  <option value="3">GitHub</option>
                </select>
                <br>
                <input type="submit" value="registrar">
            </form>

         </div>
       </div>
  </div>
</div>
</section>
</section><!--main-section-end-->
%include('footer.tpl')
