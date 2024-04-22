print("Hello world")

function fact(n)
    if n==0 then
        return 1
    else
        return n * fact(n - 1)
    end
end

print("Enter a number")
a = io.read("*number") -- this is due to different position of this file to workspace root, I think so 😅
print(fact(a))

function Div(el)
    return el.content
    
end