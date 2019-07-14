<?php
ini_set("display_errors", "On"); 

composer require mashape/unirest-php

$response = Unirest\Request::post("https://textanalysis-keyword-extraction-v1.p.rapidapi.com/keyword-extractor-text",
  array(
    "X-RapidAPI-Host" => "textanalysis-keyword-extraction-v1.p.rapidapi.com",
    "X-RapidAPI-Key" => "2777e48392msh433c74269a5da3bp187f8djsn3077dc11238c",
    "Content-Type" => "application/x-www-form-urlencoded"
  ),
  array(
    "text" => "Keyword extraction is tasked with the automatic identification of terms that best describe the subject of a document. Key phrases, key terms, key segments or just keywords are the terminology which is used for defining the terms that represent the most relevant information contained in the document. Although the terminology is different, function is the same: characterization of the topic discussed in a document. Keyword extraction task is important problem in Text Mining, Information Retrieval and Natural Language Processing. Keyword assignment vs. extraction Keyword assignment methods can be roughly divided into: keyword assignment (keywords are chosen from controlled vocabulary or taxonomy) and keyword extraction (keywords are chosen from words that are explicitly mentioned in original text). Methods for automatic keyword extraction can be: supervised, semi-supervised and unsupervised. Unsupervised methods can be further divided into: simple statistics, linguistics, graph-based and other methods.",
    "wordnum" => 5
  )
);

echo $response;
	
?>