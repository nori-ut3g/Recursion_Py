# 連邦税を設定します。
federalTaxes = 0.2;


# 州の税率を受け取って、所得を受け取り所得税を計算する関数を返す、関数を作成します。
def taxLambda(stateTax, state):
    def f(income):
        # 連邦税、州税の変数はどちらもスコープ外です。
        # この関数が作成されると、stateTax および federalTaxes の状態が何であれ、この関数にバインドされます。作成時の stateTax が 0.15 である場合、この関数の stateTax の状態は 0.15 になります。
        taxes = federalTaxes + stateTax
        print("Computing taxes for state..." + state)
        return int(income - (taxes * income));

    return f


californiaF = taxLambda(0.0725, "California")
texasF = taxLambda(0.0625, "Texas")
hawaiiF = taxLambda(0.04, "Hawaii")

# 税金を計算します。
income = 40000
print("Calculating income using lambdas")
print(californiaF(income))
print(texasF(income))
print(hawaiiF(income))

income2 = 500000;
print("------Calculating more income using lambdas------")
print(californiaF(income2))
print(texasF(income2))
print(hawaiiF(income2))