from conans import ConanFile, CMake, tools
import os
import sys

class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if tools.cross_building(self.settings):
            return
        
        self.run(os.path.join('bin', 'test_package'), run_environment=True)

