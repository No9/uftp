{
  "targets": [
    {
      "target_name": "uftp",
      "sources": [ "src/uftp.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}