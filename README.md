# Homologación de Universidades


Cuando los candidatos postulan a un aviso, ingresan la información de la universidad de diversas formas y esto hace que sea muy difícil saber exactamente la agrupación por universidades. 

En el archivo **instituciones_educativas.csv** se ha tomado una muestra de lo que escriben los candidatos cuando postulan a un aviso.
Por otro lado, se sabe que en SUNEDU hay un número limitado de universidades licencias. En el archivo **universidades.json** se tiene la información de todas las universidades peruanas en formato JSON.


Elaborar un algoritmo que permita homologar la universidades que se encuentran en el archivo **instituciones_educativas.csv** tomando como referencia las universidades que se encuentran en **universidades.json**. 

De tal manera que se generen los siguiente archivos:


**universidades_homologadas.csv**: con los siguientes campos: candidateId, value, universidad homologada


**sinonimo_universidades.json**: con la siguiente estrutura:
<code>
[
	{
		nombre_universidad: "Universidad César Vallejo S.A.C."
		sinonimos: [ 'ucv', "cesar vallejo", "cesar vallejo (ucv)"]
	}
]
</code>

**Ficheros**:


+ [universidades.json](https://krowdy.s3.us-east-1.amazonaws.com/ats/job/6434447e8e6c4c0008808420/opentest/2023-04-11T04-36-09-824ZUniversidades.json)
+ [instituciones_educativas.csv](#)
