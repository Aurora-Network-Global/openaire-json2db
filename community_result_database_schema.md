# Root
| ColumnName | DataType | Description |
|------------|----------|-------------|
| author | array |  |
| bestaccessright | object |  |
| codeRepositoryUrl | string |  |
| collectedfrom | array |  |
| contactgroup | array |  |
| contactperson | array |  |
| container | object |  |
| context | array |  |
| contributor | array |  |
| country | array |  |
| coverage | array |  |
| dateofcollection | string |  |
| description | array |  |
| documentationUrl | array |  |
| embargoenddate | string |  |
| format | array |  |
| geolocation | array |  |
| id | string |  |
| indicators | object |  |
| instance | array |  |
| language | object |  |
| lastupdatetimestamp | integer |  |
| maintitle | string |  |
| originalId | array |  |
| pid | array |  |
| programmingLanguage | string |  |
| projects | array |  |
| publicationdate | string |  |
| publisher | string |  |
| size | string |  |
| source | array |  |
| subjects | array |  |
| subtitle | string |  |
| tool | array |  |
| type | string |  |
| version | string |  |

# author
| ColumnName | DataType | Description |
|------------|----------|-------------|
| fullname | string |  |
| name | string |  |
| pid | array |  |
| rank | integer |  |
| surname | string |  |

# pid
| ColumnName | DataType | Description |
|------------|----------|-------------|
| id | string |  |
| provenance | array |  |

# id
| ColumnName | DataType | Description |
|------------|----------|-------------|
| scheme | string |  |
| value | string |  |

# bestaccessright
| ColumnName | DataType | Description |
|------------|----------|-------------|
| code | string | COAR access mode code: http://vocabularies.coar-repositories.org/documentation/access_rights/ |
| label | string | Label for the access mode |
| scheme | string | Scheme of reference for access right code. Always set to COAR access rights vocabulary: http://vocabularies.coar-repositories.org/documentation/access_rights/ |

# container
| ColumnName | DataType | Description |
|------------|----------|-------------|
| conferencedate | string |  |
| conferenceplace | string |  |
| edition | string | Edition of the journal or conference proceeding |
| ep | string | End page |
| iss | string | Journal issue number |
| issnLinking | string |  |
| issnOnline | string |  |
| issnPrinted | string |  |
| name | string | Name of the journal or conference |
| sp | string | Start page |
| vol | string | Volume |

# context
| ColumnName | DataType | Description |
|------------|----------|-------------|
| code | string |  |
| label | string |  |
| provenance | array |  |

# country
| ColumnName | DataType | Description |
|------------|----------|-------------|
| code | string |  |
| label | string |  |
| provenance | array |  |

# geolocation
| ColumnName | DataType | Description |
|------------|----------|-------------|
| box | string |  |
| place | string |  |
| point | string |  |

# indicators
| ColumnName | DataType | Description |
|------------|----------|-------------|
| bipIndicators | array | The impact measures (i.e. popularity) |
| usageCounts | object | The usage counts (i.e. downloads) |

# bipIndicators
| ColumnName | DataType | Description |
|------------|----------|-------------|
| clazz | string |  |
| indicator | string |  |
| score | string |  |

# usageCounts
| ColumnName | DataType | Description |
|------------|----------|-------------|
| downloads | string |  |
| views | string |  |

# instance
| ColumnName | DataType | Description |
|------------|----------|-------------|
| accessright | object |  |
| alternateIdentifier | array |  |
| articleprocessingcharge | object |  |
| collectedfrom | array |  |
| hostedby | unknown |  |
| license | string |  |
| pid | array |  |
| publicationdate | string |  |
| refereed | string |  |
| type | string |  |
| url | array |  |

# accessright
| ColumnName | DataType | Description |
|------------|----------|-------------|
| code | string |  |
| label | string |  |
| openAccessRoute | string |  |
| scheme | string |  |

# alternateIdentifier
| ColumnName | DataType | Description |
|------------|----------|-------------|
| scheme | string |  |
| value | string |  |

# articleprocessingcharge
| ColumnName | DataType | Description |
|------------|----------|-------------|
| amount | string |  |
| currency | string |  |

# language
| ColumnName | DataType | Description |
|------------|----------|-------------|
| code | string | alpha-3/ISO 639-2 code of the language |
| label | string | Language label in English |

# projects
| ColumnName | DataType | Description |
|------------|----------|-------------|
| acronym | string |  |
| code | string |  |
| funder | object |  |
| id | string |  |
| provenance | array |  |
| title | string |  |
| validated | object |  |

# funder
| ColumnName | DataType | Description |
|------------|----------|-------------|
| fundingStream | string |  |
| jurisdiction | string |  |
| name | string |  |
| shortName | string |  |

# validated
| ColumnName | DataType | Description |
|------------|----------|-------------|
| validatedByFunder | boolean |  |
| validationDate | string |  |

# subjects
| ColumnName | DataType | Description |
|------------|----------|-------------|
| provenance | array |  |
| subject | object |  |

# subject
| ColumnName | DataType | Description |
|------------|----------|-------------|
| scheme | string |  |
| value | string |  |

