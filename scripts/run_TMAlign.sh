
# From the local directory.
f=(*.pdb)

mkdir -p TMAlignResults

for ((i = 0; i < ${#f[@]}; i++)); do
      for ((j = i + 1; j < ${#f[@]}; j++)); do
          #echo "${f[i]} - ${f[j]}";
          
          OUTPUT=TMAlignResults/"${f[i]}_AND_${f[j]}.txt"
          
          if [ "${#OUTPUT}" -ge 255 ]; then
             #rename_file
             temp=TMAlignResults/"${f[i]}_AND_${f[j]}.txt"
             temp2="${temp:0:250}.txt"
             OUTPUT=$temp2
          fi
                      
          echo "# Output: "$OUTPUT
          
          #tmalign "${f[i]}" "${f[j]}" -a -o $OUTPUT
          #tmalign "${f[i]}" "${f[j]}" -a -m $OUTPUT | tee $OUTPUT
          tmalign "${f[i]}" "${f[j]}" -a | tee $OUTPUT
      done;
done
