#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
    ofBackground(255,255,255);
}

//--------------------------------------------------------------
void ofApp::draw(){
    ofSetColor(54, 60, 146);    //blue
    ofDrawTriangle(680, 414, 295, 776, 1067, 776);  //first mountain
    ofDrawTriangle(928, 564, 563, 834, 1292, 834);  //second mountain
    ofSetColor(255, 255, 255);  //white
    ofDrawTriangle(680, 432, 590, 522, 770, 522);   //snow on first mountain
    ofDrawTriangle(928, 599, 630, 843, 1226, 843);  //front of second mountain
    ofSetColor(54, 60, 146);    //blue
    ofDrawCircle(418, 1024, 437);   //stupa border
    ofDrawRectangle(291, 439, 203, 172);    //face border
    ofDrawTriangle(393, -17, 296, 441, 489, 441);   //shrine
    ofSetColor(255, 255, 255);  //white
    ofDrawCircle(419, 1024, 402);   //stupa front
    ofDrawRectangle(307, 461, 167, 138);    //face front
    ofSetColor(221, 0, 39); //red
    ofDrawTriangle(393, 370, 337, 441, 449, 441);   //head top
    ofSetColor(255, 255, 255);  //white
    ofDrawTriangle(393, 389, 353, 441, 433, 441);  //head top light
    ofSetColor(221, 0, 39); //red
    ofDrawRectangle(281, 439, 223, 27); //head hat
    ofSetColor(255, 255, 255);  //white
    ofDrawRectangle(0, 539, 433, 485);  //mask
    ofSetColor(221, 0, 39); //red
    ofDrawRectangle(22, 783, 472, 31);  //bottom beam
    ofSetColor(54, 60, 146); //blue
    ofDrawTriangle(252, 609, 27, 776, 477, 776); //bottom layer
    ofSetColor(255, 255, 255);  //white
    ofDrawRectangle(137, 633, 229, 32); //gap
    ofSetColor(221, 0, 39); //red
    ofDrawRectangle(92, 607, 314, 26);  //top beam
    ofSetColor(54, 60, 146);
    ofDrawTriangle(247, 461, 98, 598, 395, 598);    //top layer
    ofSetColor(255, 255, 255);  //white
    ofDrawTriangle(247, 461, 190, 511, 303, 511);   //gap
    //gap in shrine
    ofDrawRectangle(306, 72, 178, 14);
    ofDrawRectangle(306, 91, 178, 14);
    ofDrawRectangle(306, 109, 178, 14);
    ofDrawRectangle(306, 127, 178, 18);
    ofDrawRectangle(306, 154, 178, 18);
    ofDrawRectangle(306, 177, 178, 18);
    ofDrawRectangle(306, 200, 178, 18);
    ofDrawRectangle(306, 227, 178, 18);
    ofDrawRectangle(306, 257, 178, 18);
    ofDrawRectangle(306, 287, 178, 18);
    ofDrawRectangle(306, 323, 178, 18);
    ofDrawRectangle(306, 355, 178, 18);

    ofSetColor(54, 60, 146);    //blue
    ofDrawTriangle(246, 466, 228, 499, 263, 499);   //shrine
    
    //Text
    ofDrawRectangle(19, 834, 45, 150);
    ofDrawRectangle(167, 834, 45, 150);
    ofDrawRectangle(370, 834, 49, 150);
    ofDrawRectangle(300, 834, 189, 37);
    ofDrawRectangle(579, 834, 48, 150);
    ofDrawRectangle(709, 834, 46, 150);
    ofDrawRectangle(579, 890, 176, 37);
    ofDrawRectangle(579, 947, 176, 37);
    ofDrawRectangle(579, 834, 176, 37);
    ofDrawTriangle(62.5, 835.5, 170.5, 923.5, 173.5, 982.5);
    ofDrawTriangle(62.5, 835.5, 62.5, 900.5, 173.5, 982.5);
}
