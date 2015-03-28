Title: Eclipse error: HttpServlet was not found
Date: 2014-05-01
Category: Java, Eclipse
Tags: build path, eclipse, http, java, jsp, maven, servlet, tomcat
Slug: httpservlet-was-not-found
Authors: rafaelbarrelo
Summary: Eclipse error: HttpServlet was not found

Criei um projeto Maven no Eclipse e logo de cara recebi o erro no JSP:

>The superclass “javax.servlet.http.HttpServlet” was not found on the Java Build Path

Em uma busca rápida no Google, achei a solução no StackOverflow:

1. Click com o botão direito no projeto
2. Selecione: Build Path > Configure Build Path..
3. Selecione a aba Libraries
4. Click em Add Library.. > Server Runtime > Apache Tomcat > Finish.
5. Click em OK e pronto!

No meu caso, esses passos resolveram a questão da dependência que faltava. Mas caso não resolva, existem mais 2 opções que podem ser encontrada aqui: http://stackoverflow.com/questions/22756153/httpservlet-was-not-found



> Esse post foi publicado originalmente no meu antigo blog em WordPress
