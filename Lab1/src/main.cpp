#include "ofMain.h"
#include "ofApp.h"

int main( ){

	ofGLWindowSettings settings;
	settings.setSize(1024, 1024);
	settings.windowMode = OF_WINDOW;

	auto window = ofCreateWindow(settings);

	ofRunApp(window, make_shared<ofApp>());
	ofRunMainLoop();

}
