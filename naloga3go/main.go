package main

import (
	"fmt"
	"go/token"
	"go/types"
	"strings"
)

func contains(s []string, e string) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}

func join(arr []string) string {
	return strings.Join(arr[:], "")
}

func calculate(t string) bool {
	// expression, err := govaluate.NewEvaluableExpression(t)
	// if err != nil {
	// 	fmt.Println(err.Error())
	// 	return false
	// }

	// parameters := make(map[string]interface{}, 8)

	// result, err := expression.Evaluate(parameters)
	// if err != nil {
	// 	fmt.Println(err.Error())
	// 	return false
	// }

	fs := token.NewFileSet()
	tv, err := types.Eval(fs, nil, token.NoPos, fmt.Sprintf("(%s) == 100", t))
	if err != nil {
		panic(err)
	}

	fmt.Println(t, tv.Value.String())

	return tv.Value.String() == "true"
}

func recursive(t []string, seznamResitev []string, alreadyTried []string) []string {
	foundNone := false
	for i := 0; i < len(t); i++ {
		k := t[i]
		if k == "" {
			foundNone = true
			break
		}
	}

	if !foundNone {
		return seznamResitev
	}

	for i := 0; i < len(t); i++ {
		v := t[i]
		if v != "" {
			continue
		}

		d1 := make([]string, 0)
		d1 = append(d1, t...)
		d2 := make([]string, 0)
		d2 = append(d2, t...)

		d1[i] = "-"
		d2[i] = "+"

		d := [][]string{d1, d2}

		for n := 0; n < len(d); n++ {
			v := d[n]
			_t := join(v)

			if contains(alreadyTried, _t) {
				continue
			}

			if calculate(_t) && !contains(seznamResitev, _t) {
				seznamResitev = append(seznamResitev, _t)
			}

			alreadyTried = append(alreadyTried, _t)
			seznamResitev = recursive(v, seznamResitev, alreadyTried)
		}
	}

	return seznamResitev
}

func main() {
	seznamResitev := make([]string, 0)
	zaporedje := [...]string{"1", "", "2", "", "3", "", "4", "", "5", "", "6", "", "7", "", "8", "", "9"}
	alreadyTried := make([]string, 0)

	fmt.Println(recursive(zaporedje[:], seznamResitev, alreadyTried))
}
