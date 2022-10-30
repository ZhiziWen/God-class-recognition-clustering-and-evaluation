import javalang
import pandas as pd
from javalang.tree import FieldDeclaration

def get_fields(java_class):
    fields = []
    for field in java_class.fields:
        fields.append(field.declarators[0].name)
    return fields

def get_method(java_class):
    methods = []
    for method in java_class.methods:
        methods.append(method.name)
    return methods

def get_fields_accessed_by_method(method):
    members = []
    for path, node in method:
        if type(node) is javalang.tree.MemberReference and not node.qualifier == '':
            members.append(node.qualifier)
        elif type(node) is javalang.tree.MemberReference and node.qualifier == '':
            members.append(node.member)
    return members

def get_methods_accessed_by_method(method):
    members = []
    for path, node in method:
        if type(node) is javalang.tree.MethodInvocation:
            members.append(node.member)
    return members

if __name__ == "__main__":
    # God class: CoreDocumentImpl, DTDGrammar, XSDHandler, XIncludeHandler
    file_name = "CoreDocumentImpl" # add the name of god class here
    java_file = f'./{file_name}.java'
    f = open(java_file, 'r')
    f_read = f.read()
    tree = javalang.parse.parse(f_read)

    fields_list = {}
    methods_list = {}

    for path, node in tree:
        if type(node) is javalang.tree.ClassDeclaration and node.name == f'{file_name}': # Only god class, no inner class
            fields = {}
            methods = {}
            fields = fields.fromkeys(get_fields(node), 0) # find all fields, remove replication of same name fields
            methods = methods.fromkeys(get_method(node), 0) # find all methods, remove replication of same name methods
            for method in node.methods:
                fields_in_methods = get_fields_accessed_by_method(method) # find all fields in one method
                methods_in_methods = get_methods_accessed_by_method(method) # find all methods used in one method
                for field in fields_in_methods:
                   if field in fields:
                        fields[field] = 1
                for met in methods_in_methods:
                   if met in methods:
                        methods[met] = 1
                fields_list[method.name] = fields
                methods_list[method.name] = methods
                fields = fields.fromkeys(fields, 0) # reset fields dictionary
                methods = methods.fromkeys(methods, 0) # reset methods dictionary

    df_fields = pd.DataFrame.from_dict(fields_list, orient='index')
    df_method = pd.DataFrame.from_dict(methods_list, orient='index')
    result = pd.concat([df_fields, df_method], axis=1)
    result = result.loc[:, (result != 0).any(axis=0)] # Keep only columns which have at least one non 0 value
    print(result)
    result.to_csv(f"{file_name}_FeatureVector.csv")
