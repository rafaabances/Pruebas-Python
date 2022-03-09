# Para realizar exáctamente lo mismo en C#, necesitamos de 3 librerías, y unas 25-30 líneas en total:

<code>using System;
 using System.Net;
 using System.IO;</code>
 <code>
 namespace ConsoleApplication1
 {
 class Program
 {
 static void Main(string[] args)
 {
 Console.WriteLine( getSourceCode("http://www.google.es"));
 Console.ReadLine();
 }</code>
 <code>
 private static string getSourceCode(string uri)
 {
 string sourceCode = "";
 try
 { HttpWebRequest request = (HttpWebRequest)WebRequest.Create(uri);
 HttpWebResponse response = (HttpWebResponse)request.GetResponse();
 StreamReader sr = new StreamReader(response.GetResponseStream());
 sourceCode = sr.ReadToEnd();
 sr.Close();
 response.Close();
 return sourceCode; }
 catch
 { sourceCode = "ERROR"; }
 return sourceCode;
 } } }</code>