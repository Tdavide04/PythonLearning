import codecs

testo_cifrato = "synt{7u3_134f7_p4a_j4gpu_7u3_s10j_j4ea3!}"
testo_decifrato = codecs.encode(testo_cifrato, "rot_13")

print("Testo decifrato:", testo_decifrato) #flag

