employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
             "JACKSON Peter","JOHNSON Rick",
             "LEWIS Terry","CLARKE Robin"]

empj = list(filter(lambda e: e[0] =="J", employees))

print("\n".join(empj))