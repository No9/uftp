{'targets': [{
    'target_name': 'uftp', 
	'variables': {
        'uftpversion': '4.7'
    }, 
    'type': 'static_library',
    # Overcomes an issue with the linker and thin .a files on SmartOS
    'standalone_static_library': 1,
	}]
}