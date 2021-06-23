#!/usr/bin/env bash

function tablica()
{
  awk 'BEGIN {
    fruits["mango"] = "yellow";
    fruits["orange"] = "orange";
    fruits["apple"] = "red";
    print fruits["orange"]
  }'

  #delete array[index]
}

function tablica_2d()
{
  awk 'BEGIN {
    arr["0,0"] = 100;
    arr["0,1"] = 200;
    arr["0,2"] = 300;
    arr["1,0"] = 400;
    arr["1,1"] = 500;
    arr["1,2"] = 600;
    arr["2,0"] = 700;
    arr["2,1"] = 800;
    arr["2,2"] = 900;

    print "arr[0,0] = "arr["0,0"];
    print "arr[0,1] = "arr["0,1"];
    print "arr[0,2] = "arr["0,2"];
    print "arr[1,0] = "arr["1,0"];
    print "arr[1,1] = "arr["1,1"];
    print "arr[1,2] = "arr["1,2"];
    print "arr[2,0] = "arr["2,0"];
    print "arr[2,1] = "arr["2,1"];
    print "arr[2,2] = "arr["2,2"];

  }'
}

#main
#tablica
tablica_2d