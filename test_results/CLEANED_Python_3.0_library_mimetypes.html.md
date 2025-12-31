

# `mimetypes` — Map filenames to MIME types[¶](https://docs.python.org/3.0/library/mimetypes.html#module-mimetypes "Permalink to this headline")
The `mimetypes` module converts between a filename or URL and the MIME type associated with the filename extension. Conversions are provided from filename to MIME type and from MIME type to filename extension; encodings are not supported for the latter conversion.
The module provides one class and a number of convenience functions. The functions are the normal interface to this module, but some applications may be interested in the class as well.
The functions described below provide the primary interface for this module. If the module has not been initialized, they will call [`init()`](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.init "mimetypes.init") if they rely on the information [`init()`](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.init "mimetypes.init") sets up.

`mimetypes.``guess_type`(_filename_[, _strict_])[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.guess_type "Permalink to this definition")

Guess the type of a file based on its filename or URL, given by _filename_. The return value is a tuple `(type, encoding)` where _type_ is `None` if the type can’t be guessed (missing or unknown suffix) or a string of the form `'type/subtype'`, usable for a MIME _content-type_ header.
_encoding_ is `None` for no encoding or the name of the program used to encode (e.g. **compress** or **gzip**). The encoding is suitable for use as a _Content-Encoding_ header, _not_ as a _Content-Transfer-Encoding_ header. The mappings are table driven. Encoding suffixes are case sensitive; type suffixes are first tried case sensitively, then case insensitively.
Optional _strict_ is a flag specifying whether the list of known MIME types is limited to only the official types [registered with IANA](http://www.iana.org/assignments/media-types/) are recognized. When _strict_ is true (the default), only the IANA types are supported; when _strict_ is false, some additional non-standard but commonly used MIME types are also recognized.

`mimetypes.``guess_all_extensions`(_type_[, _strict_])[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.guess_all_extensions "Permalink to this definition")

Guess the extensions for a file based on its MIME type, given by _type_. The return value is a list of strings giving all possible filename extensions, including the leading dot (`'.'`). The extensions are not guaranteed to have been associated with any particular data stream, but would be mapped to the MIME type _type_ by [`guess_type()`](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.guess_type "mimetypes.guess_type").
Optional _strict_ has the same meaning as with the [`guess_type()`](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.guess_type "mimetypes.guess_type") function.

`mimetypes.``guess_extension`(_type_[, _strict_])[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.guess_extension "Permalink to this definition")

Guess the extension for a file based on its MIME type, given by _type_. The return value is a string giving a filename extension, including the leading dot (`'.'`). The extension is not guaranteed to have been associated with any particular data stream, but would be mapped to the MIME type _type_ by [`guess_type()`](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.guess_type "mimetypes.guess_type"). If no extension can be guessed for _type_ , `None` is returned.
Optional _strict_ has the same meaning as with the [`guess_type()`](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.guess_type "mimetypes.guess_type") function.
Some additional functions and data items are available for controlling the behavior of the module.

`mimetypes.``init`([_files_])[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.init "Permalink to this definition")
    Initialize the internal data structures. If given, _files_ must be a sequence of file names which should be used to augment the default type map. If omitted, the file names to use are taken from [`knownfiles`](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.knownfiles "mimetypes.knownfiles"). Each file named in _files_ or [`knownfiles`](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.knownfiles "mimetypes.knownfiles") takes precedence over those named before it. Calling [`init()`](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.init "mimetypes.init") repeatedly is allowed.

`mimetypes.``read_mime_types`(_filename_)[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.read_mime_types "Permalink to this definition")
    Load the type map given in the file _filename_ , if it exists. The type map is returned as a dictionary mapping filename extensions, including the leading dot (`'.'`), to strings of the form `'type/subtype'`. If the file _filename_ does not exist or cannot be read, `None` is returned.

`mimetypes.``add_type`(_type_ , _ext_[, _strict_])[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.add_type "Permalink to this definition")

Add a mapping from the mimetype _type_ to the extension _ext_. When the extension is already known, the new type will replace the old one. When the type is already known the extension will be added to the list of known extensions.
When _strict_ is True (the default), the mapping will added to the official MIME types, otherwise to the non-standard ones.

`mimetypes.``inited`[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.inited "Permalink to this definition")
    Flag indicating whether or not the global data structures have been initialized. This is set to true by [`init()`](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.init "mimetypes.init").

`mimetypes.``knownfiles`[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.knownfiles "Permalink to this definition")

List of type map file names commonly installed. These files are typically named `mime.types` and are installed in different locations by different packages.

`mimetypes.``suffix_map`[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.suffix_map "Permalink to this definition")
    Dictionary mapping suffixes to suffixes. This is used to allow recognition of encoded files for which the encoding and the type are indicated by the same extension. For example, the `.tgz` extension is mapped to `.tar.gz` to allow the encoding and type to be recognized separately.

`mimetypes.``encodings_map`[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.encodings_map "Permalink to this definition")
    Dictionary mapping filename extensions to encoding types.

`mimetypes.``types_map`[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.types_map "Permalink to this definition")
    Dictionary mapping filename extensions to MIME types.

`mimetypes.``common_types`[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.common_types "Permalink to this definition")
    Dictionary mapping filename extensions to non-standard, but commonly found MIME types.
The [`MimeTypes`](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.MimeTypes "mimetypes.MimeTypes") class may be useful for applications which may want more than one MIME-type database:

class `mimetypes.``MimeTypes`([_filenames_])[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.MimeTypes "Permalink to this definition")

This class represents a MIME-types database. By default, it provides access to the same database as the rest of this module. The initial database is a copy of that provided by the module, and may be extended by loading additional `mime.types`-style files into the database using the [`read()`](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.MimeTypes.read "mimetypes.MimeTypes.read") or [`readfp()`](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.MimeTypes.readfp "mimetypes.MimeTypes.readfp") methods. The mapping dictionaries may also be cleared before loading additional data if the default data is not desired.
The optional _filenames_ parameter can be used to cause additional files to be loaded “on top” of the default database.
An example usage of the module:
```


['/etc/mime.types', '/etc/httpd/mime.types', ... ]
'.tar.gz'
'gzip'
'application/x-tar-gz'

```

## MimeTypes Objects[¶](https://docs.python.org/3.0/library/mimetypes.html#id1 "Permalink to this headline")
[`MimeTypes`](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.MimeTypes "mimetypes.MimeTypes") instances provide an interface which is very like that of the `mimetypes` module.

`MimeTypes.``suffix_map`[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.MimeTypes.suffix_map "Permalink to this definition")
    Dictionary mapping suffixes to suffixes. This is used to allow recognition of encoded files for which the encoding and the type are indicated by the same extension. For example, the `.tgz` extension is mapped to `.tar.gz` to allow the encoding and type to be recognized separately. This is initially a copy of the global `suffix_map` defined in the module.

`MimeTypes.``encodings_map`[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.MimeTypes.encodings_map "Permalink to this definition")
    Dictionary mapping filename extensions to encoding types. This is initially a copy of the global `encodings_map` defined in the module.

`MimeTypes.``types_map`[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.MimeTypes.types_map "Permalink to this definition")
    Dictionary mapping filename extensions to MIME types. This is initially a copy of the global `types_map` defined in the module.

`MimeTypes.``common_types`[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.MimeTypes.common_types "Permalink to this definition")
    Dictionary mapping filename extensions to non-standard, but commonly found MIME types. This is initially a copy of the global `common_types` defined in the module.

`MimeTypes.``guess_extension`(_type_[, _strict_])[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.MimeTypes.guess_extension "Permalink to this definition")
    Similar to the [`guess_extension()`](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.guess_extension "mimetypes.guess_extension") function, using the tables stored as part of the object.

`MimeTypes.``guess_type`(_url_[, _strict_])[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.MimeTypes.guess_type "Permalink to this definition")
    Similar to the [`guess_type()`](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.guess_type "mimetypes.guess_type") function, using the tables stored as part of the object.

`MimeTypes.``read`(_path_)[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.MimeTypes.read "Permalink to this definition")
    Load MIME information from a file named _path_. This uses [`readfp()`](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.MimeTypes.readfp "mimetypes.MimeTypes.readfp") to parse the file.

`MimeTypes.``readfp`(_file_)[¶](https://docs.python.org/3.0/library/mimetypes.html#mimetypes.MimeTypes.readfp "Permalink to this definition")
    Load MIME type information from an open file. The file must have the format of the standard `mime.types` files.
### [Table Of Contents](https://docs.python.org/3.0/contents.html)
  * [`mimetypes` — Map filenames to MIME types](https://docs.python.org/3.0/library/mimetypes.html)
    * [MimeTypes Objects](https://docs.python.org/3.0/library/mimetypes.html#id1)


#### Previous topic
[`mailbox` — Manipulate mailboxes in various formats](https://docs.python.org/3.0/library/mailbox.html "previous chapter")
#### Next topic
[`base64` — RFC 3548: Base16, Base32, Base64 Data Encodings](https://docs.python.org/3.0/library/base64.html "next chapter")
### This Page
  * [Show Source](https://docs.python.org/3.0/_sources/library/mimetypes.txt)


### Quick search
Enter search terms or a module, class or function name.
### Navigation
  * [index](https://docs.python.org/3.0/genindex.html "General Index")
  * [modules](https://docs.python.org/3.0/modindex.html "Global Module Index") |
  * [next](https://docs.python.org/3.0/library/base64.html "base64 — RFC 3548: Base16, Base32, Base64 Data Encodings") |
  * [previous](https://docs.python.org/3.0/library/mailbox.html "mailbox — Manipulate mailboxes in various formats") |
  * ![](https://docs.python.org/3.0/_static/py.png)
  * [Python v3.0.1 documentation](https://docs.python.org/3.0/index.html) »
  * [The Python Standard Library](https://docs.python.org/3.0/library/index.html) »
  * [Internet Data Handling](https://docs.python.org/3.0/library/netdata.html) »


© [Copyright](https://docs.python.org/3.0/copyright.html) 1990-2009, Python Software Foundation. Last updated on Feb 14, 2009. Created using [Sphinx](http://sphinx.pocoo.org/) 0.6.