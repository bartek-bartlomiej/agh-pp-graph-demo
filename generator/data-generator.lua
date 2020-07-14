local args = {...}
local nodes_number = tonumber(args[1])
assert(nodes_number, "Expecting number of nodes")

local elements = {}

for i = 1, nodes_number do
    local node = string.format('{ "data": { "id": "%d" } }', i)
    table.insert(elements, node)
end

for line in io.lines() do
    local _, _, i, j = string.find(line, "^(%d+)%s+(%d+)")
    local edge = string.format('{ "data" : { "id": "%d-%d", "source": "%d", "target": "%d" } }', i, j, i, j)
    table.insert(elements, edge)
end

io.write("[\n"..table.concat(elements, ",\n").."\n]")
