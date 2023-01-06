import re
someregix=re.compile('foo',re.IGNORECASE | re.DOTALL)
someregix=re.compile('foo',re.IGNORECASE | re.DOTALL |re.VERBOSE)  #The re.VERBOSE flag has several effects. Whitespace
                                                                    # in the regular expression that isn't inside a character class is ignored.
                                                                        #This means that an expression such