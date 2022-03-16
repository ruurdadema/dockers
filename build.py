#!/usr/bin/env python3 -u
import subprocess


def build_image(source, name, push: bool):
    subprocess.run(['docker', 'build', source, '-t', name])
    if push:
        subprocess.run(['docker', 'push', name])


def main():
    build_image('juce-build-linux', 'ruurdadema/juce-build-linux', push=True)
    build_image('juce-build-linux-amd64', 'ruurdadema/juce-build-linux-amd64', push=True)
    build_image('juce-build-linux-arm64v8', 'ruurdadema/juce-build-linux-arm64v8', push=True)


if __name__ == '__main__':
    print("Invoke {} as script".format(__file__))
    main()
