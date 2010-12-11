from xml.dom import minidom

def make_proccpu_sim(dom) :
    tempstring = "";
    tempstring = tempstring + "/*this file is auto_generated by volk_register.py*/\n\n";
    tempstring = tempstring + "#include <volk/volk_cpu.h>\n"
    tempstring = tempstring + "#include <stdio.h>\n"
    tempstring = tempstring + "\n\n"

    tempstring = tempstring + "void test_append(char* buf,  int val, char* newkey){\n";
    tempstring = tempstring + "    if(val==1){\n";
    tempstring = tempstring + "        sprintf(buf, \"%s %s\", buf, newkey);\n";
    tempstring = tempstring + "    }\n";
    tempstring = tempstring + "}\n";
    tempstring = tempstring + "\n\n";
    
    tempstring = tempstring + "int main() {\n";
    tempstring = tempstring + "    volk_cpu_init();\n";
    tempstring = tempstring + "    char buf[2048];\n";
    for domarch in dom:
        arch = str(domarch.attributes["name"].value);
        tempstring = tempstring + "    test_append(buf, volk_cpu.has_" + arch + "(), \"" + arch + "\");\n"
    tempstring = tempstring + "    printf(\"%s\\n\", buf);\n"
    tempstring = tempstring + "}\n"
    return tempstring;
