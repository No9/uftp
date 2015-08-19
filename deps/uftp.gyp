{'targets': [{
    'target_name': 'libuftp', 
	'variables': {
        'uftpversion': '4.7'
    },
    'conditions': [
        ['OS == "win"', {
            'defines': ['WINDOWS', 'OPENSSL'],
            "msvs_settings": {
                  "VCCLCompilerTool": {
                      "RuntimeTypeInfo": "false"
                    , "EnableFunctionLevelLinking": "true"
                    , "ExceptionHandling": "2"
                    , "DisableSpecificWarnings": [ "4355", "4530" ,"4267", "4244", "4506", "4024", "4047", "4018"]
                  }
              },
            'conditions': [
            # "openssl_root" is the directory on Windows of the OpenSSL files.
            # Check the "target_arch" variable to set good default values for
            # both 64-bit and 32-bit builds of the module.
            ['target_arch=="x64"', 
              { 'variables': { 'openssl_root%': 'C:/OpenSSL-Win64' } }, 
              { 'variables': { 'openssl_root%': 'C:/OpenSSL-Win32' } }
            ]
          ],
          'libraries': [  '-l<(openssl_root)/lib/libeay32.lib' ],
          'include_dirs': [ '<(openssl_root)/include' ],
          'ccflags': ['-Zi', '-W3', ' -nologo', '-Od'],
          'link_settings': {
            'ldflags': ['/IGNORE:4006']
          },
        }]
    ],
    'type': 'static_library',
    # Overcomes an issue with the linker and thin .a files on SmartOS
    'standalone_static_library': 1,
	'sources': [
        "uftp-<(uftpversion)/client.h",
        "uftp-<(uftpversion)/client_announce.c",
        "uftp-<(uftpversion)/client_announce.h",
        "uftp-<(uftpversion)/client_common.c",
        "uftp-<(uftpversion)/client_common.h",
        "uftp-<(uftpversion)/client_config.c",
        "uftp-<(uftpversion)/client_config.h",
        "uftp-<(uftpversion)/client_fileinfo.c",
        "uftp-<(uftpversion)/client_fileinfo.h",
        "uftp-<(uftpversion)/client_init.c",
        "uftp-<(uftpversion)/client_init.h",
        "uftp-<(uftpversion)/client_loop.c",
        "uftp-<(uftpversion)/client_loop.h",
        "uftp-<(uftpversion)/client_main.c",
        "uftp-<(uftpversion)/client_transfer.c",
        "uftp-<(uftpversion)/client_transfer.h",
        "uftp-<(uftpversion)/encrypt_cng.c",
        "uftp-<(uftpversion)/encrypt_cryptoapi.c",
        "uftp-<(uftpversion)/encrypt_none.c",
        "uftp-<(uftpversion)/encrypt_openssl.c",
        "uftp-<(uftpversion)/encryption.h",
        "uftp-<(uftpversion)/heartbeat_send.c",
        "uftp-<(uftpversion)/heartbeat_send.h",
        "uftp-<(uftpversion)/proxy.h",
        "uftp-<(uftpversion)/proxy_common.c",
        "uftp-<(uftpversion)/proxy_common.h",
        "uftp-<(uftpversion)/proxy_config.c",
        "uftp-<(uftpversion)/proxy_config.h",
        "uftp-<(uftpversion)/proxy_downstream.c",
        "uftp-<(uftpversion)/proxy_downstream.h",
        "uftp-<(uftpversion)/proxy_init.c",
        "uftp-<(uftpversion)/proxy_init.h",
        "uftp-<(uftpversion)/proxy_loop.c",
        "uftp-<(uftpversion)/proxy_loop.h",
        "uftp-<(uftpversion)/proxy_main.c",
        "uftp-<(uftpversion)/proxy_upstream.c",
        "uftp-<(uftpversion)/proxy_upstream.h",
        "uftp-<(uftpversion)/server.h",
        "uftp-<(uftpversion)/server_announce.c",
        "uftp-<(uftpversion)/server_announce.h",
        "uftp-<(uftpversion)/server_common.c",
        "uftp-<(uftpversion)/server_common.h",
        "uftp-<(uftpversion)/server_config.c",
        "uftp-<(uftpversion)/server_config.h",
        "uftp-<(uftpversion)/server_init.c",
        "uftp-<(uftpversion)/server_init.h",
        "uftp-<(uftpversion)/server_main.c",
        "uftp-<(uftpversion)/server_phase.c",
        "uftp-<(uftpversion)/server_phase.h",
        "uftp-<(uftpversion)/server_send.c",
        "uftp-<(uftpversion)/server_send.h",
        "uftp-<(uftpversion)/server_transfer.c",
        "uftp-<(uftpversion)/server_transfer.h",
        "uftp-<(uftpversion)/uftp.1",
        "uftp-<(uftpversion)/uftp.h",
        "uftp-<(uftpversion)/uftp_common.c",
        "uftp-<(uftpversion)/uftp_common.h",
        "uftp-<(uftpversion)/uftp_keymgt.1",
        "uftp-<(uftpversion)/uftp_keymgt.c",
        "uftp-<(uftpversion)/uftpd.1",
        "uftp-<(uftpversion)/uftpproxyd.1",
        "uftp-<(uftpversion)/win_func.c",
        "uftp-<(uftpversion)/win_func.h",
        ],
    }]
}