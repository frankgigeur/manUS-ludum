#define HS422_CNT_SERVO_MIN 120   // Compteur minimum du PWM 12bit du PCA9865 pour le servomoteur HS422 (0°).
#define HS422_CNT_SERVO_MID 307     // Compteur millieu du PWM 12bit du PCA9865 pour le servomoteur HS422 (90°).
#define HS422_CNT_SERVO_MAX 525     // Compteur maximum du PWM 12bit du PCA9865 pour le servomoteur HS422 (180°).
#define HS422_US_MIN  489           // L'équivalent en us du compteur minimum pour le PWM 12bit du PCA9865 pour le servomoteur HS422 (0°).
#define HS422_US_MID  1506          // L'équivalent en us du compteur millieu pour le PWM 12bit du PCA9865 pour le servomoteur HS422 (90°).
#define HS422_US_MAX  2563          // L'équivalent en us du compteur maximum pour le PWM 12bit du PCA9865 pour le servomoteur HS422 (180°).

/* paramètre d'ajustement du module pca9865 */
#define HS422_SERVO_FREQ 50         // Fréquence du PMW pour le servomoteur HS422.
#define PCA9685_OSC_FREQ 25100401   // Fréquence d'oscillation du PCA9865 (Ajusté pour avoir une fréquence de 50Hz précisément).

/* pouce */
#define HS422_po_inc_comp 480       // inclinaison complète
#define HS422_po_inc_init 270       // inclinaison initial
#define HS422_po_ext_comp 250      // extension complète

/* index */
#define HS422_in_inc_comp 320       // inclinaison complète
#define HS422_in_inc_init 130       // inclinaison initial
#define HS422_in_ext_comp 95       // extension complète

/* majeur */
#define HS422_ma_inc_comp 500       // inclinaison complète
#define HS422_ma_inc_init 140       // inclinaison initial
#define HS422_ma_ext_comp 95       // extension complète

/* annulaire */
#define HS422_an_inc_comp 470       // inclinaison complète
#define HS422_an_inc_init 130       // inclinaison initial
#define HS422_an_ext_comp 100       // extension complète

/* petit doigt */
#define HS422_pd_inc_comp 370       // inclinaison complète
#define HS422_pd_inc_init 130       // inclinaison initial
#define HS422_pd_ext_comp 110       // extension complète

/* ID/OUTPUT des doigts sur le PCA9865 */
#define ID_pouce 2                  // moteur ID du pouce
#define ID_index 3                  // moteur ID de l'index
#define ID_majeur 4                 // moteur ID du majeur
#define ID_annulaire 5              // moteur ID annulaire
#define ID_petitdoigt 6             // moteur ID du petit doigt


#define cnt_SERVO_reach 235         // reach
#define cnt_SERVO_half_reach 170    // half reach
