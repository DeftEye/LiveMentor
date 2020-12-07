require 'json'
require 'set'
require 'csv'

def find_Endpoints(node, key= "O", key_String="")
    if node.class == hash
        leavenode = {}
        for node_key in node.keys()
            if key_String == ""
                bis_Key_String = node_key
            else
                bis_Key_String = key_String + "." + str(node_key)
            end
        node.update(find_Endpoints(node[node_key], node_key, bis_Key_String))
        return node
        end
    end
    if node.class == Array
        node = {}
        str_array = ""
        for elem in node
            str_array += elem.to_s + ", "
            str_array = str_array[:-2]
        end
        if len(elements) > 0
            node[key] = str_array
        end
        return node
    end
    else
        return {key_String: node}
    end
end


file = File.read('./test.json')
f_input = JSON.parse(file)
fieldnames = Set.new

for entry in f_input
    fieldnames += find_Endpoints(entry).keys()
end


CSV.open("output.csv", "w") do |csv|
    for entry in f_input
        csv << fieldnames
    end
    for entry in f_input
        csv << find_Endpoints(entry)
    end
end