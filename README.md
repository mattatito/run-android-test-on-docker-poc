
## Android tests Poc

### Objective:
- Run local android test inside a docker image with an emulator

### Learned

I've tried to up the docker image that runs emulator in Github Actions, but unfortunately, 
Github Actions doesn't allow users to use hardware acceleration (KVM in linuxOS and HAXM in macOS).
The android emulator needs this to run.

### Running project

