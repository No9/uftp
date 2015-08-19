{
  "targets": [
    {
      "target_name": "uftp",
      "sources": [ "src/uftp.cc" ],
      "include_dirs": [ "<!(node -e \"require('nan')\")"],
      "dependencies": ["<(module_root_dir)/deps/uftp.gyp:libuftp"],
      'conditions': [
        ['OS == "win"', {
            "msvs_settings": {
                  "VCCLCompilerTool": {
                      "RuntimeTypeInfo": "false"
                    , "EnableFunctionLevelLinking": "true"
                    , "ExceptionHandling": "2"
                    , "DisableSpecificWarnings": [ "4355", "4530" ,"4267", "4244", "4006"]
                  }
              },
          'ccflags': ['-Zi', '-W3', ' -nologo', '-Od'],
          'link_settings': {
            'ldflags': ['/IGNORE:4006']
          },
        }]
      ],
    }
  ]
}