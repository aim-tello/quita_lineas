# quita_lineas
Programa que lee un archivo de texto (file1) y usa las líneas de file1 para buscar en otro archivo (file2) y borrarlas si corresponden con los patrones de file1

Una opción que sustituye este script, para linux es: 

```
$ diff -u file2.txt file1.txt | egrep '^-/';
```

Gracias a @dabicho por la referencia
