package main
import "fmt"
func s(z,c,d int){
if z>0{s(z-1,c,c^d)
fmt.Println(c,"->",d)
s(z-1,c^d,d)}}
func main(){s(9,1,3)}
