package teste;

import java.awt.Component;
import javax.swing.JOptionPane;

public class jogo
{
    public static void main(final String[] args) {
        int n = 0;
        for (int i = 0; i < 10; ++i) {
            n = (int)(Math.random() * 3.0) + 1;
        }
        final int resposta = JOptionPane.showConfirmDialog(null, "VAMOS JOGAR");
        if (resposta == 0) {
            if (n == 1) {
                JOptionPane.showMessageDialog(null, "Rocket League");
            }
            if (n == 2) {
                JOptionPane.showMessageDialog(null, "MM");
            }
            if (n == 3) {
                JOptionPane.showMessageDialog(null, "GC");
            }
            else {
                System.exit(0);
            }
        }
    }
}