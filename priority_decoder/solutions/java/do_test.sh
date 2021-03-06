#!/bin/sh

BASE="$(dirname "$0")"
TESTCASES="$BASE/../../testcases/"

cd "$BASE"
rm *.class
javac priority_decoder.java

for testcase in "$TESTCASES"/*.input ; do
	printf "Running test $(basename "$testcase")... "
	RESULT_FILE="/tmp/$(uuidgen)"
	ERR="$(java priority_decoder < "$testcase" 1> "$RESULT_FILE") 2>&1"
	DIFF="$(diff "$TESTCASES/$(basename "$testcase" .input).output" "$RESULT_FILE")"
	if [ "$(echo "$DIFF" | wc -l)" != "1" ] ; then
		echo "FAIL"
		echo "Difference between output and expected: "
		echo "$DIFF" | while read -r ln ; do
			echo -e "\t$ln"
		done
		echo ""
	else
		echo "PASSED"
	fi
	rm -f "$RESULT_FILE"
done

